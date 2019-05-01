<template>
  <div id="app">
    <RepoSelector @repo-selected='onRepoSelected'/>
    <h1>{{ repo }}</h1>
    <grid-layout
            :layout.sync="layout"
            :col-num="12"
            :row-height="30"
            :is-draggable="true"
            :is-resizable="true"
            :is-mirrored="false"
            :vertical-compact="true"
            :margin="[10, 10]"
            :use-css-transforms="true"
    >

        <grid-item v-for="item in layout"
                   :x="item.x"
                   :y="item.y"
                   :w="item.w"
                   :h="item.h"
                   :i="item.i">
            <component :is="item.c" :repo="repo"></component>

        </grid-item>
    </grid-layout>
  </div>
</template>

<script>
import PullRequest from './components/plot/PullRequest.vue'
import RepoSelector from './components/RepoSelector.vue'
import VueGridLayout from 'vue-grid-layout';
import { VueAutosuggest } from 'vue-autosuggest';
import pr_data from './assets/data/pr_avg_lifespan_2016_2018.json'


export default {
  name: 'app',
  components: {
    PullRequest,
    RepoSelector,
    VueAutosuggest,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem
  },
  data(){
    return {
      layout: [
        {"x":0,"y":0,"w":5,"h":10,"i":"1","c":"PullRequest", "p":{repo:"BelooS/ChipsLayoutManager"} },
    	],
      repo: 'elastic/elasticsearch'
    }
  },
  methods: {
    onRepoSelected(repo) {
        this.repo = repo;
    },
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
