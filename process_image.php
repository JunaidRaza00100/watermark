<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {
    $imagePath = 'uploads/' . basename($_FILES['image']['name']);
    
    // Move the uploaded image to the uploads directory
    if (move_uploaded_file($_FILES['image']['tmp_name'], $imagePath)) {
        $outputPath = 'processed/' . basename($_FILES['image']['name']);
        
        // Load the uploaded image
        $image = imagecreatefromjpeg($imagePath);

        // Simple effect to blur the watermark area (not effective for all watermarks)
        for ($i = 0; $i < 5; $i++) {
            imagefilter($image, IMG_FILTER_GAUSSIAN_BLUR);
        }

        // Save the processed image
        imagejpeg($image, $outputPath);
        imagedestroy($image);

        echo $outputPath;
    } else {
        http_response_code(500);
        echo "Failed to upload image";
    }
} else {
    http_response_code(400);
    echo "No image uploaded";
}
?>
