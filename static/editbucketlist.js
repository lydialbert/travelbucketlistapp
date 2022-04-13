// My Bucketlist Page //

'use strict';

// Delete Buttons for My Bucketlists Page. //

const deleteButtons = document.querySelectorAll('.delete_button');

for (const button of deleteButtons) {
    button.addEventListener('click', (evt) => { 
        alert("Bucket list has been deleted.")

        const formInputs = {
            bucketlist_id: button.id,
          };
        
          fetch('/delete_bucketlist', {
            method: 'POST',
            body: JSON.stringify(formInputs),
            headers: {
              'Content-Type': 'application/json',
            },
          })
            .then(response => response.text())
            .then(responseText => {
                console.log(responseText);
                if (responseText == "Success") {
                    document.querySelector(`#div${button.id}`).remove();
                }
        });
    });
}