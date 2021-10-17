<template>
  <div>
    <canvas id="chart"></canvas>
  </div>
</template>

<script>

import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);
import moment from "moment";
import axios from "axios";


export default {
  data() {
    return {
      chart: null,
      this_day_last_year: moment().subtract(1, 'years'),
      chart_data: {
        type: "line",
        data: {
          labels: [
            
          ],
          datasets: [
            {
              label: "Doanh thu bán hàng Bosch",
              data: [
                ],
              borderColor: "#AF495d",
              borderWidth: 3,
            },
            {
              label: "Lợi nhuận bán hàng Bosch",
              data: [

              ],
              borderColor: "#BBb784",
              borderWidth: 3,
            },
            {
              label: "Tổng lợi nhuận kế toán trước thuế",
              data: [
              ],
              borderColor: "#47b784",
              borderWidth: 3,
            },
            {
              label: "Tổng giá trị nhập kho",
              data: [
              ],
              borderColor: "#FFb784",
              borderWidth: 3,
            }
          ],
        },
        options: {
          responsive: true,
          lineTension: 0.4,
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  padding: 125,
                },
              },
            ],
          },
        },
      },
    };
  },
  async mounted() {
    const ctx = document.getElementById("chart");
    this.chart = new Chart(ctx, this.chart_data);
    console.log(this.chart)
    this.addData(this.this_day_last_year)
  },
  methods: {
    async addData(month) {
      
      let url = new URL(process.env.VUE_APP_API_ENDPOINT + "/api/v1/business-results")
      url.searchParams.set("start", month.startOf("month").format("YYYY-MM-DD"))
      url.searchParams.set("end", month.endOf("month").format("YYYY-MM-DD"))
      let component = this
      
      await axios.get(url.href, {}).then((response) => {
        let label = month.format("MM-YYYY")
        console.log(month.startOf("month").format("YYYY-MM-DD"))
        component.chart.data.labels.push(label);
        component.chart.data.datasets[0].data.push(response.data[0].value)
        component.chart.data.datasets[1].data.push(response.data[4].value)
        component.chart.data.datasets[2].data.push(response.data[11].value)
        component.chart.data.datasets[3].data.push(response.data[20].value)
        console.log(response.data[0].value)
        component.chart.update();
      });
      if (month < moment().subtract(1, 'M')){
        this.addData(month.add(1, "M"))
      }
    }
  }
};
</script>
