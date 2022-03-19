// Event Listeners for the Travel Bucketlist App. //

'use strict';

// Add Button //

const addButton = document.querySelector('#suggestion_button');

addButton.addEventListener('click', (evt) => {
    evt.preventDefault();

    alert('Added to Your Bucketlist!')
});

function mounted() {
    new google.maps.places.Autocomplete(
        document.getElementById("autocomplete")
    )
};