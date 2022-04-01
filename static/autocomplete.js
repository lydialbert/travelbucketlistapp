// Google Places Auto-Complete. //

<script>
let autocomplete;
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('autocomplete'), 
        {
            types: ['establishment'],
            fields: ['place_id', 'geomtry', 'name']
        })};
</script>

autocomplete.addListener('place_changed', onPlaceChanged);

function onPlaceChanged() {
    var place = autocomplete.getPlace();

    if (!place.geometry) {
        document.getElementById('autocomplete').placeholder =
        'Enter a place';
    } else {
        // Display details about the vaild place
        document.getElementById('details').innerHTML = place.name
    }
}