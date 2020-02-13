<template>
  <div id="app">
    <router-view/>
  </div>  
</template>



<style>
html,
body {
  height: 100%;
}

body {
  background: radial-gradient(
      circle at center,
      rgba(255, 255, 255, 0.3),
      rgba(0, 0, 0, 0.3)
    ),
    url(https://tinyurl.com/s867htn);
  background-repeat: no-repeat, repeat;
  background-size: cover, auto;

  overflow: hidden;
}

#app {
  font-family: "Staatliches", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
