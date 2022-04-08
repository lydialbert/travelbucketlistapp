// Event Listeners for the Travel Bucketlist App. //

'use strict';

// Account Button for Welcome Page. //

const createAccountButton = document.querySelector('#create_account_button');

createAccountButton.addEventListener('click', (evt) => {
    alert('Success! Go ahead and login in.')
});

// Login Button for Welcome Page. //

const loginButton = document.querySelector('#login_button');

loginButton.addEventListener('click', (evt) => {
    alert('Welcome back!')
});

// Forgot Password Link. //

const linkButton = document.querySelector('#link');

linkButton.addEventListener('click', (evt) => {
    alert('Reset Password link was sent to your email - check your inbox!')
});