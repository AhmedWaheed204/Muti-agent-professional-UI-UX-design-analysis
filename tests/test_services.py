import pytest
from io import BytesIO
from src.services.image_service import ImageService

def test_image_processing():
    fake_image = BytesIO(b"fake image data")
    fake_image.name = "test.png"
    processed = ImageService.process_uploaded_files([fake_image])
    assert len(processed) == 1
    assert processed[0].endswith(".png")

def test_invalid_image_processing():
    fake_image = BytesIO(b"invalid data")
    fake_image.name = "test.jpg"
    with pytest.raises(ValueError):
        ImageService.process_uploaded_files([fake_image])