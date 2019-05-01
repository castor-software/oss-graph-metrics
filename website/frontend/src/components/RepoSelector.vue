<template>
  <vue-autosuggest
      :suggestions="filteredOptions"
      @selected="onRepoSelected"
      :input-props="{id:'autosuggest__input', onInputChange:this.onInputChange, placeholder:'Do you feel lucky, punk?'}"
  >
    <template slot-scope="{suggestion}">
      <span class="my-suggestion-item">{{suggestion.item}}</span>
    </template>
  </vue-autosuggest>
</template>

<script>
import { VueAutosuggest } from 'vue-autosuggest';
import pr_data from '../assets/data/pr_avg_lifespan_2016_2018.json'


export default {
  name: 'RepoSelector',
  components: {
    VueAutosuggest,
  },
  data(){
    return {
      options: [{
          data: Object.keys(pr_data)
        }],
      filteredOptions: [],
      repo: 'elastic/elasticsearch'
    }
  },
  methods: {
    onRepoSelected(option) {
      this.repo = option.item;
      this.$emit('repo-selected', this.repo);
    },
    onInputChange(text) {
      console.log(text)
        if (text === '' || text === undefined) {
          return;
        }

        /* Full control over filtering. Maybe fetch from API?! Up to you!!! */
        const filteredData = this.options[0].data.filter(item => {
          return item.toLowerCase().indexOf(text.toLowerCase()) > -1;
        }).slice(0, this.limit);

        this.filteredOptions = [{
          data: filteredData
        }];
      }
  },
}
</script>

<style>
#autosuggest__input {
  outline: none;
  position: relative;
  display: block;
  font-family: monospace;
  font-size: 20px;
  border: 1px solid #616161;
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
}

#autosuggest__input.autosuggest__input-open {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

.autosuggest__results-container {
  position: relative;
  width: 100%;
}

.autosuggest__results {
  font-weight: 300;
  margin: 0;
  position: absolute;
  z-index: 10000001;
  width: 100%;
  border: 1px solid #e0e0e0;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
  background: white;
  padding: 0px;
  overflow: scroll;
  max-height: 200px;
}

.autosuggest__results ul {
  list-style: none;
  padding-left: 0;
  margin: 0;
}

.autosuggest__results .autosuggest__results_item {
  cursor: pointer;
  padding: 15px;
}

#autosuggest ul:nth-child(1) > .autosuggest__results_title {
  border-top: none;
}

.autosuggest__results .autosuggest__results_title {
  color: gray;
  font-size: 11px;
  margin-left: 0;
  padding: 15px 13px 5px;
  border-top: 1px solid lightgray;
}

.autosuggest__results .autosuggest__results_item:active,
.autosuggest__results .autosuggest__results_item:hover,
.autosuggest__results .autosuggest__results_item:focus,
.autosuggest__results .autosuggest__results_item.autosuggest__results_item-highlighted {
  background-color: #ddd;
}
</style>
