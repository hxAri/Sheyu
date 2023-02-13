#!/bin/bash

# Usage:
#   encrypt.sh [-e|-d] [-s <algorithm>] [-p <algorithm>] <file>

# Constants
PRIVATE_KEY=private_key.pem
PUBLIC_KEY=public_key.pem
SYMMETRIC_ALGORITHMS=(aes-128-cbc aes-128-ecb aes-192-cbc aes-192-ecb aes-256-cbc aes-256-ecb bf bf-cbc bf-cfb bf-ecb bf-ofb camellia-128-cbc camellia-128-ecb camellia-192-cbc camellia-192-ecb camellia-256-cbc camellia-256-ecb des des-cbc des-cfb des-ecb des-ede des-ede-cbc des-ede-cfb des-ede-ofb des-ede3 des-ede3-cbc des-ede3-cfb des-ede3-ofb des-ofb des3 desx seed seed-cbc)
PUBLIC_KEY_ALGORITHMS=(rsa dsa dh ecdh ecdsa)

# Parse command line arguments
while getopts "e:d:s:p:" opt; do
  case $opt in
    e)
      mode=encrypt
      ;;
    d)
      mode=decrypt
      ;;
    s)
      symmetric_algorithm=$OPTARG
      ;;
    p)
      public_key_algorithm=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Shift the parsed options
shift $((OPTIND-1))

# Check for valid input
if [ -z "$mode" ]; then
  echo "Error: Must specify either encryption (-e) or decryption (-d)" >&2
  exit 1
fi
if [ -z "$symmetric_algorithm" ] && [ -z "$public_key_algorithm" ]; then
  echo "Error: Must specify a symmetric (-s) or public-key (-p) algorithm" >&2
  exit 1
fi
if [ -n "$symmetric_algorithm" ] && [ -n "$public_key_algorithm" ]; then
  echo "Error: Cannot specify both a symmetric (-s) and public-key (-p) algorithm" >&2
  exit 1
fi
if [ -n "$symmetric_algorithm" ] && [[ ! " ${SYMMETRIC_ALGORITHMS[@]} " =~ " ${symmetric_algorithm} " ]]; then
  echo "Error: Invalid symmetric algorithm: $symmetric_algorithm" >&2
  exit 1
fi
if [ -n "$public_key_algorithm" ] && [[ ! " ${PUBLIC_KEY_ALGORITHMS[@]} " =~ " ${public_key_algorithm} " ]]; then
  echo "Error: Invalid public-key algorithm: $public_key_algorithm" >&2
  exit 1
fi
if [ $# -ne 1 ]; then
  echo "Error: Must specify a file to $mode" >&2
  exit 1
fi

file=$1

# Symmetric encryption
if [ -n "$symmetric_algorithm" ]; then
  if [ "$mode" == "encrypt" ]; then
    openssl $symmetric_algorithm -a -salt -in $file -out "$file.enc"
  elif [ "$mode" == "decrypt" ]; then
    openssl $symmetric_algorithm -d -a -in "$file.enc" -out "$file.dec"
  fi
fi

# Public-key encryption
if [ -n "$public_key_algorithm" ]; then
  if [ "$mode" == "encrypt" ]; then
    # Generate key pair if necessary
    if [ ! -f $PRIVATE_KEY ] || [ ! -f $PUBLIC_KEY ]; then
      openssl genpkey -algorithm $public_key_algorithm -out $PRIVATE_KEY
      openssl pkey -pubout -in $PRIVATE_KEY -out $PUBLIC_KEY
    fi

    openssl pkeyutl -encrypt -in $file -out "$file.enc" -pubin -inkey $PUBLIC_KEY
  elif [ "$mode" == "decrypt" ]; then
    openssl pkeyutl -decrypt -in "$file.enc" -out "$file.dec" -inkey $PRIVATE_KEY
  fi
fi
