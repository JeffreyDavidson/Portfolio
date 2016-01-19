<?php

/*
*  List of colleges interested by my sister to attend.
*/
$colleges = array(
	array(
		'name' => 'University of Kansas', 
		'distance' => 1286.9
	),
	array(
		'name' => 'University of Florida', 
		'distance' => 120.3
	),
	array(
		'name' => 'Emporia State University', 
		'distance' => 1352.1
	),
	array(
		'name' => 'University of Central Florida', 
		'distance' => 7.6
	),
	array(
		'name' => 'Florida State University',
		'distance' => 254.4
	)
);

// Listed out colleges array in human readable format.
echo '<pre>';
print_r($colleges);
echo '</pre>';

// Array of colleges passed to sort_alphabetically function and printed out to screen.
$alphabetically = $colleges;
usort($alphabetically, 'sort_by_name');
echo '<pre>';
print_r($alphabetically);
echo '</pre>';

$distanced = $colleges;
usort($distanced, 'sort_by_distance_closest_to_me');
echo '<pre>';
print_r($distanced);
echo '</pre>';


/**
 * Function for returning provided array alphabetically
 *
 * @param array $colleges Array of colleges visited.
 * @param array $colleges Array of colleges visited.
 *
 * @return array $colleges Alphabetically sorted array.
 */
function sort_by_name($a, $b) {
	return strnatcmp($a['name'], $b['name']);
}

/**
 * Function for returning provided array alphabetically
 *
 * @param array $colleges Array of colleges visited.
 * @param array $colleges Array of colleges visited.
 *
 * @return array $colleges Alphabetically sorted array.
 */
function sort_by_distance_closest_to_me($a, $b) {
	return strnatcmp($a['distance'], $b['distance']);
}

?>