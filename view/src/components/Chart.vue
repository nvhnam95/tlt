<template>
  <div>
    <canvas id="chart"></canvas>
  </div>
</template>

<script>

import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  data() {
    return {
      chart_data: {
        type: "line",
        data: {
          labels: [
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune",
          ],
          datasets: [
            {
              label: "Number of Moons",
              data: [0, 0, 1, 2, 79, 82, 27, 14],
              backgroundColor: "rgba(54,73,93,.5)",
              borderColor: "#36495d",
              borderWidth: 3,
            },
            {
              label: "Planetary Mass (relative to the Sun x 10^-6)",
              data: [
                0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514,
              ],
              backgroundColor: "rgba(71, 183,132,.5)",
              borderColor: "#47b784",
              borderWidth: 3,
            },
          ],
        },
        options: {
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  padding: 25,
                },
              },
            ],
          },
        },
      },
    };
  },
  mounted() {
    // axios.get(url, { params }).then((response) => {
    //     console.log(response.data)
    //   });
    const ctx = document.getElementById("chart");
    console.log(this.chart_data)
    let chart = new Chart(ctx, this.chart_data);
    let component = this
    setTimeout(function() {
      component.addData(chart, "Test", 30 )
    }, 1000);

  },
  methods:{
    addData(chart, label, data) {
      chart.data.labels.push(label);
      chart.data.datasets.forEach((dataset) => {
          dataset.data.push(data);
      });
      chart.update();
    }
  }
};
</script>