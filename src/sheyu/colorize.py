
from re import compile, MULTILINE, match, Match, Pattern as BasePattern, S, split, sub as substr
from sys import maxsize as Maxsize
from typing import Any, Dict, List


class Colorize:
	
	RegExp:Dict[str,Dict[str,Any]] = {
		"number": {
			"pattern": r"(?P<number>\b(?:\d+)\b)",
			"colorize": "\x1b[1;38;5;61m{}{}"
		},
		"define": {
			"handler": lambda matched: substr( r"(\.|\-){1,}", lambda m: "\x1b[1;38;5;69m{}\x1b[1;38;5;111m".format( m.group() ), matched.group( 0x0 ) ),
			"pattern": r"(?P<define>(?:@|\$)[a-zA-Z0-9_\-\.]+)",
			"colorize": "\x1b[1;38;5;111m{}{}"
		},
		"symbol": {
			"pattern": r"(?P<symbol>\\|\:|\*|-|\+|/|&|%|=|\;|,|\.|\?|\!|\||<|>|\~){1,}",
			"colorize": "\x1b[1;38;5;69m{}{}"
		},
		"bracket": {
			"pattern": r"(?P<bracket>\{|\}|\[|\]|\(|\)){1,}",
			"colorize": "\x1b[1;38;5;214m{}{}"
		},
		"boolean": {
			"pattern": r"(?P<boolean>\b(?:False|True|None)\b)",
			"colorize": "\x1b[1;38;5;199m{}{}"
		},
		"typedef": {
			"pattern": r"(?P<typedef>\b(?:ABCMeta|AbstractSet|Annotated|Any|AnyStr|ArithmeticError|AssertionError|AsyncContextManager|AsyncGenerator|AsyncIterable|AsyncIterator|AttributeError|Awaitable|BaseException|BinaryIO|BlockingIOError|BrokenPipeError|BufferError|ByteString|BytesWarning|Callable|ChainMap|ChildProcessError|ClassVar|Collection|Concatenate|ConnectionAbortedError|ConnectionError|ConnectionRefusedError|ConnectionResetError|Container|ContextManager|Coroutine|Counter|DefaultDict|DeprecationWarning|Deque|Dict|EOFError|Ellipsis|EncodingWarning|EnvironmentError|Exception|False|FileExistsError|FileNotFoundError|Final|FloatingPointError|ForwardRef|FrozenSet|FutureWarning|Generator|GeneratorExit|Generic|GenericAlias|Hashable|IO|IOError|ImportError|ImportWarning|IndentationError|IndexError|InterruptedError|IsADirectoryError|ItemsView|Iterable|Iterator|KT|Key|KeyError|KeyboardInterrupt|KeysView|List|Literal|LookupError|Mapping|MappingView|Match|MemoryError|MethodDescriptorType|MethodWrapperType|ModuleNotFoundError|MutableMapping|MutableSequence|MutableSet|NameError|NamedTuple|NamedTupleMeta|NewType|NoReturn|None|NotADirectoryError|NotImplemented|NotImplementedError|OSError|Optional|OrderedDict|OverflowError|ParamSpec|ParamSpecArgs|ParamSpecKwargs|Pattern|PendingDeprecationWarning|PermissionError|ProcessLookupError|Protocol|RecursionError|ReferenceError|ResourceWarning|Reversible|RuntimeError|RuntimeWarning|Sequence|Set|Sized|StopAsyncIteration|StopIteration|SupportsAbs|SupportsBytes|SupportsComplex|SupportsFloat|SupportsIndex|SupportsInt|SupportsRound|SyntaxError|SyntaxWarning|SystemError|SystemExit|T|TabError|Text|TextIO|TimeoutError|True|Tuple|Type|TypeAlias|TypeError|TypeGuard|TypeVar|TypedDict|UnboundLocalError|UnicodeDecodeError|UnicodeEncodeError|UnicodeError|UnicodeTranslateError|UnicodeWarning|Union|UserWarning|Val|alueError|ValuesView|Warning|WrapperDescriptorType|ZeroDivisionError|abs|abstractmethod|aiter|all|anext|any|ascii|bin|bool|breakpoint|bytearray|bytes|callable|cast|chr|classmethod|collections|compile|complex|contextlib|copyright|credits|delattr|dict|dir|divmod|enumerate|eval|exec|exit|filter|final|float|format|frozenset|functools|getattr|globals|hasattr|hash|help|hex|id|input|int|io|isinstance|issubclass|iter|len|license|list|locals|map|max|memoryview|min|next|object|oct|open|operator|ord|overload|pow|print|property|quit|range|re|repr|reversed|round|set|setattr|slice|sorted|staticmethod|str|sum|super|sys|tuple|type|types|vars|zip)\b)",
			"colorize": "\x1b[1;38;5;213m{}{}"
		},
		"linked": {
			"handler": lambda matched: substr( r"(\\|\:|\*|-|\+|/|&|%|=|\;|,|\.|\?|\!|\||<|>|\~){1,}", lambda m: "\x1b[1;38;5;69m{}\x1b[1;38;5;43m".format( m.group() ), matched.group( 0x0 ) ),
			"pattern": r"(?P<linked>\bhttps?://[^\s]+)",
			"colorize": "\x1b[1;38;5;43m\x1b[4m{}{}"
		},
		"version": {
			"handler": lambda matched: substr( r"([\d\.]+)", lambda m: "\x1b[1;38;5;190m{}\x1b[1;38;5;112m".format( m.group() ), matched.group( 0x0 ) ),
			"pattern": r"(?P<version>\b[vV][\d\.]+\b)",
			"colorize": "\x1b[1;38;5;112m{}{}"
		},
		"sheyu": {
			"pattern": r"(?P<sheyu>\b(?:Sheruy[uū]tiriti|Sheyu)\b)",
			"colorize": "\x1b[1;38;5;111m{}{}"
		},
		"comment": {
			"pattern": r"(?P<comment>\#[^\n]*)",
			"colorize": "\x1b[1;38;5;250m{}{}"
		},
		"string": {
			"handler": lambda matched: substr( r"(?<!\\)(\\\"|\\\'|\\`|\\r|\\t|\\n|\\s)", lambda m: "\x1b[1;38;5;208m{}\x1b[1;38;5;220m".format( m.group() ), matched.group( 0x0 ) ),
			"pattern": r"(?P<string>(?<!\\)(\".*?(?<!\\)\"|\'.*?(?<!\\)\'|`.*?(?<!\\)`))",
			"colorize": "\x1b[1;38;5;220m{}{}"
		}
	}

	Pattern:BasePattern = compile( "(?:{})".format( "|".join( regexp['pattern'] for regexp in list( RegExp.values() ) ) ), MULTILINE|S )

	@staticmethod
	def format( string:str, base:str=None ) -> str:
		results = ""
		strings = Colorize.split( string )
		if not isinstance( base, str ):
			base = "\x1b[0m"
		try:
			last = base
			escape = None
			skipable = []
			for idx, string in enumerate( strings ):
				if idx in skipable:
					continue
				color = match( r"^(?:\x1b|\033)\[([^m]+)m$", string )
				if color is not None:
					index = idx +0x1
					escape = color.group( 0x0 )
					last = escape
					try:
						rescape = match( r"(?:\x1b|\033)\[([^m]+)m", strings[index] )
						while rescape is not None:
							skipable.append( index )
							escape += rescape.group( 0x0 )
							last = rescape.group( 0x0 )
							index += 0x1
							rescape = match( r"(?:\x1b|\033)\[([^m]+)m", strings[index] )
					except IndexError:
						break
					if index + 0x1 in skipable:
						index += 0x1
					skipable.append( index )
				else:
					escape = last
					index = idx
				string = strings[index]
				search = 0x0
				matched = Colorize.search( string, search )
				while matched is not None:
					if matched.groupdict():
						group = None
						groups = matched.groupdict().keys()
						for group in groups:
							if group in Colorize.RegExp and \
								isinstance( Colorize.RegExp[group], dict ) and \
								isinstance( matched.group( group ), str ):
								colorize = Colorize.RegExp[group]['colorize']
								break
						chars = matched.group( 0x0 )
						if "rematch" in Colorize.RegExp[group] and isinstance( Colorize.RegExp[group]['rematch'], dict ):
							pass
						if "handler" in Colorize.RegExp[group] and callable( Colorize.RegExp[group]['handler'] ):
							result += escape
							result += string[search:matched.end() - len( chars )]
							result += colorize.format( Colorize.RegExp[group]['handler']( matched ), escape )
							search = matched.end()
							matched = Colorize.search( string, search )
							continue
						result += escape
						result += string[search:matched.end() - len( chars )]
						result += colorize.format( chars, escape )
						search = matched.end()
						matched = Colorize.search( string, search )
					else:
						matched = None
				result += escape
				result += string[search:]
		except Exception as e:
			raise e
		return results
	
	@staticmethod
	def search( string:str, pos:int=0, endpos:int=Maxsize ) -> Match[Any]|None:
		return Colorize.Pattern.search( string, pos, endpos )
	
	@staticmethod
	def split( string:str ) -> List[str]:
		return list( x for x in split( r"((?:\x1b|\033)\[[0-9\;]+m)", string ) if x != "" )

	...
