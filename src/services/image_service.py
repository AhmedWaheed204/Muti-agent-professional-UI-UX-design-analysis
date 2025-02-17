import tempfile
import os
from PIL import Image
from typing import List

class ImageService:
    """Service for handling image processing and validation."""
    
    @staticmethod
    def process_uploaded_files(uploaded_files: List) -> List[str]:
        """
        Process and validate uploaded image files.
        
        Args:
            uploaded_files: List of uploaded file objects
            
        Returns:
            List of temporary file paths
        """
        processed_paths = []
        for file in uploaded_files:
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                    tmp.write(file.getvalue())
                    temp_path = tmp.name
                    Image.open(temp_path).verify()  # Validate image
                    processed_paths.append(temp_path)
            except Exception as e:
                raise ValueError(f"Invalid image file {file.name}: {str(e)}")
        return processed_paths

    @staticmethod
    def cleanup_files(file_paths: List[str]):
        """Clean up temporary image files."""
        for path in file_paths:
            try:
                os.unlink(path)
            except:
                pass