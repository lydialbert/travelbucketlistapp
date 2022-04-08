// Event Listeners for the Travel Bucketlist App. //

'use strict';

// 'Other' Feature for Bucketlist Form. //

const selectElement = document.querySelector('#category1_select');

selectElement.addEventListener('change', (evt) => {
    if (evt.target.value === 'Other') {
        document.querySelector('#category1_select').insertAdjacentHTML('afterend', 'Other: <input type="text" name="category1_choice">');
    }
});

const selectElementTwo = document.querySelector('#category2_select');

selectElementTwo.addEventListener('change', (evt) => {
    if (evt.target.value === 'Other') {
        document.querySelector('#category2_select').insertAdjacentHTML('afterend', 'Other: <input type="text" name="category2_choice">');
    }
});

const selectElementThree = document.querySelector('#category3_select');

selectElementThree.addEventListener('change', (evt) => {
    if (evt.target.value === 'Other') {
        document.querySelector('#category3_select').insertAdjacentHTML('afterend', 'Other: <input type="text" name="category3_choice">');
    }
});