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
}

$box-shadow: 0 5px 20px rgba(0,0,0,0.19), 0 3px 6px rgba(0,0,0,0.23);
$box-shadow-highlight: 0 5px 30px rgba(0,0,0,0.19), 0 3px 15px rgba(0,0,0,0.23);

$btn-color: #004D40;
$btn-color-light: #E0F2F1;
$btn-color-active: #80CBC4;
.button{
  text-decoration: none;
  width: max-content;
  margin: 20px auto;
  display: block;
  border-radius: 5px;
  box-shadow: $box-shadow;
  color: white;
  border: 2px solid $btn-color;
  background-color: $btn-color;
  transition: 0.1s;
  padding: 8px 10px;
  cursor: pointer;
  -webkit-user-select: none;  /* Chrome all / Safari all */
  -moz-user-select: none;     /* Firefox all */
  -ms-user-select: none;      /* IE 10+ */
  user-select: none;    

  &:hover{
    border: 2px solid $btn-color;
    background-color: $btn-color-light;
    color: $btn-color;
    box-shadow: $box-shadow-highlight;
  }
  &:active{
    background-color: $btn-color-active;
    border: 2px solid $btn-color-active;
  }
}
</style>
