// Event Listeners for the Travel Bucketlist App. //

'use strict';

// Add Button in suggestions.html //

const addButton = document.querySelector('#add-button');

addButton.addEventListener('click', (evt) => {
    evt.preventDefault();

    alert('Added to Your Bucketlist!')
});