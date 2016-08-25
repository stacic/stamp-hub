var stampApp = angular.module('stampApp', ['ngRoute', 'ui.bootstrap']);

stampApp.config(function($interpolateProvider, $routeProvider) {
		// Change Angular delimiter notation so it does not conflict with Jinja2
        $interpolateProvider.startSymbol('{a').endSymbol('a}');

        $routeProvider
		.when('/',
		{
			controller: 'stampCtrl',
			templateUrl: '../static/partials/stamp_list.html'
		})
		.otherwise({ redirectTo: '/' });
});

stampApp.controller('stampCtrl', function($scope, $http, $filter) {
	$http.get('/stamp/api/v1.0/stamps').success(function(data){
		$scope.stamps = data;

		$scope.filteredStamps = $scope.stamps;
		$scope.getDisplayedStamps();
	}).error(function(data){
		console.log('Error getting data in stampCtrl');
	});

	// Pagination variables
	$scope.currentPage = 1;
	$scope.stampsPerPage = 5;
	$scope.displayedStamps = [];

	$scope.getDisplayedStamps = function() {
		var begin = (($scope.currentPage - 1) * $scope.stampsPerPage);
		var end = begin + $scope.stampsPerPage;
		
		$scope.displayedStamps = $scope.filteredStamps.slice(begin, end);
	};

	$scope.pageChanged = function(){
		$scope.getDisplayedStamps();
	};

	$scope.search = function(){
		$scope.filteredStamps = $filter('filter')($scope.stamps, $scope.searchtext);
		$scope.currentPage = 1;
		$scope.getDisplayedStamps();
	};
});