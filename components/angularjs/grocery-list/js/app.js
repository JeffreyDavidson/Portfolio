function MYController($scope) {
	
	$scope.itemname = '';
	
	$scope.itemArray = [];
	
	$scope.addItem = function() {
		$scope.itemArray.push($scope.item);
		$scope.item = '';
	}
	
	$scope.deleteItem = function(deletedItem) {
		var idx = $scope.itemArray.indexOf(deletedItem);
		$scope.itemArray.splice(idx, 1);
	}
}