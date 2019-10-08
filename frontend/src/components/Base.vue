
<template>
  <div class="hello">
    <h1>{{ incs }}</h1>
    <button v-on:click="get_visitors">CLICK</button>
  </div>
</template>

<script>
const axios = require('axios').default;
export default {
  name: 'Base',
  data () {
    return {
      incs: 0
    }
  },
  methods: {
    get_visitors () {
      axios
              .get('http://localhost/get')
              .then((response) => {
        this.incs = response.data['visitors'];
      }).catch(error => console.log(error));
    }
  }}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
