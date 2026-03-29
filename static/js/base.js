console.log('js loaded')
window.onload = function () {
    // Only render chart if the container exists and data is available
    var chartContainer = document.getElementById("chartContainer");
    if (chartContainer && typeof window.chartData !== 'undefined') {
        var chart = new CanvasJS.Chart("chartContainer", {
            animationEnabled: true,
            title: {
                text: "Python Column Chart"
            },
            data: [{
                type: "column",
                dataPoints: window.chartData
            }]
        });
        chart.render();
    }
};