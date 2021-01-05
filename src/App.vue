<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
// import Batchnorm from './views/Batchnorm.vue'

export default {
  name: 'App'
  // ,
  // components: {
  //   Batchnorm
  // }
}
</script>

<style lang="scss">


$junction-dir: "assets/fonts/junction/";
@font-face {
  font-family: 'Junction';
  src: url($junction-dir+'junction-regular.eot'), /* IE9 Compat Modes */
       url($junction-dir+'junction-regular.woff') format('woff'), /* Modern Browsers */
       url($junction-dir+'junction-regular.ttf')  format('truetype'), /* Safari, Android, iOS */
}

$junction-dir: "assets/fonts/Aftasans/";
@font-face {
  font-family: 'Aftasans';
  src: url($junction-dir+'AftaSansThin-Regular.eot'), /* IE9 Compat Modes */
       url($junction-dir+'AftaSansThin-Regular.woff') format('woff'), /* Modern Browsers */
       url($junction-dir+'AftaSansThin-Regular.ttf')  format('truetype'), /* Safari, Android, iOS */
}

$junction-dir: "assets/fonts/Amaranth/";
@font-face {
  font-family: 'Amaranth';
  src: url($junction-dir+'Amaranth-Bold.eot'), /* IE9 Compat Modes */
       url($junction-dir+'Amaranth-Bold.woff') format('woff'), /* Modern Browsers */
       url($junction-dir+'Amaranth-Bold.ttf')  format('truetype'), /* Safari, Android, iOS */
}

#app {
  font-family: "Aftasans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
