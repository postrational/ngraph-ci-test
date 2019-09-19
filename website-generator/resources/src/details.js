// Details trend chart
let line_trend = document.getElementById("line_trend");
let framework_data = JSON.parse(line_trend.getAttribute("framework_data"));
let trend_data = framework_data.trend;

let labels = trend_data.map(summary => summary.date.split(' ')[0]);
let data = trend_data.map(summary => summary.passed);
let display_data_count = 15;
let line_chart_data = {
    labels: [""].concat(labels.slice(-display_data_count)),
    datasets: [{
        data: [0].concat(data.slice(-display_data_count)),
        label: "Passed",
        fill: true,
        backgroundColor: 'transparent',
        borderColor: palette.passed,
        borderWidth: 2,
        pointBackgroundColor: palette.passed
    }]
}

let line_chart = new Chart(line_trend, {
    type: 'line',
    data: line_chart_data,
    options: {
        responsive: true,
        title: {
            fontSize: 20,
            display: false,
            text: "Passed Unit Tests Trend"
        },
        legend: {
            display: false,
            position: 'bottom'
        },
        scales: {
            xAxes: [{}],
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    suggestedMin: 0,
                    suggestedMax: framework_data.coverage.total,
                },
                scaleLabel: {
                    fontSize: 20,
                    display: true,
                    labelString: "passed unit tests"
                }
            }]
        },
        elements: {
            line: {
                tension: 0 // Disables bezier curves
            }
        }
    }
});