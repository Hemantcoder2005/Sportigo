async function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var error_message = document.getElementById('error-message');

    const csrfToken = getCookie('csrftoken');

    try {
        const response = await fetch('/login/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ 'username': username, 'password': password })
        });
        const responseData = await response.json();
        console.log(responseData)
        if (responseData['response']) {
            window.location.href = "/";
        } else {
            error_message.style.color = 'red';
            error_message.innerHTML = responseData.message || "Invalid Username or Password";
        }
    } catch (error) {
        console.error('Error during login:', error);
        error_message.style.color = 'red';
        error_message.innerHTML = "An error occurred during login";
    }
}
// Function to get CSRF token from cookie
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}