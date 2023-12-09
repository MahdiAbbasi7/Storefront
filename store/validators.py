from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 100

    if file.size > max_size * 1024:
        return ValidationError(f'File size cannot be larger than {max_size}KB!')