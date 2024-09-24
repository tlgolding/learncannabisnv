<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Compose email message
    $to = "dabbyleemiller@gmail.com"; // Change to your email address
    $subject = "Message from $name";
    $body = "From: $name\nEmail: $email\n\nMessage:\n$message";

    // Send email
    if (mail($to, $subject, $body)) {
        echo "<p>Message sent successfully!</p>";
    } else {
        echo "<p>Failed to send message. Please try again later.</p>";
    }
}
?>
