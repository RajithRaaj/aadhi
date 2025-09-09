from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app) # This is important for allowing the frontend to make requests to this backend.

@app.route('/contact', methods=['POST'])
def handle_contact_form():
    """
    Handles POST requests from the contact form.
    Receives JSON data, processes it, and returns a success message.
    """
    try:
        # Check if the request body is valid JSON
        if not request.is_json:
            return jsonify({"error": "Request body must be JSON"}), 400

        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Basic validation
        if not all([name, email, message]):
            return jsonify({"error": "Missing required fields (name, email, message)"}), 400

        # --- Backend Logic Goes Here ---
        # In a real-world scenario, you would perform actions here like:
        # 1. Sending an email with the form data to your personal email.
        #    (You would use a library like `smtplib` or a service like SendGrid)
        # 2. Saving the contact message to a database.
        # 3. Performing a spam check.
        
        # For this example, we'll just log the data to the console.
        print(f"New contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        return jsonify({"message": "Thank you for your message! I'll get back to you soon."}), 200

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask app on a local development server
    # The debug=True option will reload the server automatically on code changes
    # In a production environment, you would use a production-ready server like Gunicorn or uWSGI
    app.run(debug=True, port=5000)
