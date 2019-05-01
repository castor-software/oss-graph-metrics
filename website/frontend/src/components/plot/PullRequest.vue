<template>
  <div class="hello">
    <h2>PR lifespan</h2>
    <GChart
      type="LineChart"
      :data="chartData"
      :options="chartOptions"
    />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import pr_data from '../../assets/data/pr_avg_lifespan_2016_2018.json'

export default {
  name: 'PullRequest',
  components: {
    GChart
  },
  props: {
    repo: String
  },
  watch: {
    repo: function(newVal, oldVal) { // watch it
      console.log('Prop changed: ', newVal, ' | was: ', oldVal)
      this.fetchData(newVal)
    }
  },
  data () {
    return {
      chartData:[
        ['Month', 'Lifespan (days)']
      ],
      chartOptions: {
        curveType: 'function',
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        }
      }
    }
  },
  mounted() {
    this.fetchData(this.repo)
  },
  methods: {
    fetchData(repo) {
      const month = Object.keys(pr_data[this.repo]['lifespan']);
      const chartData = month.map(function(v) {
        return [new Date(v),
          pr_data[repo]['lifespan'][v]['lifespan'] / 60 / 24,
          //pr_data[repo]['lifespan'][v]['count']
        ];
      });
      this.chartData = [
        ['Month', 'Lifespan (days)'],
        ...chartData
      ]
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
