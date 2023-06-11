#!/bin/bash
# Function to recursively list .py files
list_py_files() {
  local directory="$1"
  local markdown_file="$2"
  sed -i 's/ | score:.*$//g' "$markdown_file"
  # Loop through files and directories in the given directory
  for file in "$directory"/*; do
    if [[ -f "$file" && "${file##*.}" == "py" ]]; then
      # Parse the filename to remove extension and keep last part
      filename="${file##*/}"
      filename="${filename%.*}"

      # Get the byte count of the file
      byte_count=$(wc -c < "$file")
      # Print the parsed filename and byte count
      echo "Filename: $filename"
      echo "Byte Count: $byte_count"
      echo
      # Update the line in the Markdown file with the byte count
      sed -i "/$filename/s/\[ ]/[x]/g" "$markdown_file"
      sed -i "s/\($filename.*\)/\1 | score: $byte_count/" "$markdown_file"

    elif [[ -d "$file" ]]; then
      # Recursively call the function for subdirectories
      list_py_files "$file" "$markdown_file"
    fi
  done
}

# Check if the Markdown file argument is provided
if [[ $# -eq 1 ]]; then
  # Call the function to list .py files in the current directory
  list_py_files "." "$1"
else
  echo "Please provide the Markdown file as an argument."
fi