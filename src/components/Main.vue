<template>
  <div class='hello'>

  <!-- NAVIGATION BAR-->

      <v-toolbar color='primary' height="75vh" flat=true>
        <router-link to='/'>
          <v-toolbar-title>Project ZenGen</v-toolbar-title>
        </router-link>

        <v-spacer></v-spacer>
        <v-toolbar-side-icon><v-img src="https://tinyurl.com/s8ly94f" min-height='75' min-width='75' height='17vh' width='17vh'></v-img></v-toolbar-side-icon>
        <v-spacer></v-spacer>

        <v-toolbar-items>
          <v-btn  text width=10w to='/login'>Login</v-btn>
          <v-btn text width=10w to="/register">Sign Up</v-btn>
        </v-toolbar-items>
      </v-toolbar>
    
  <!-- MAIN STUFF-->
  </div>
</template>

<script>

export default {
  name: "Main"
};
</script>

<style scoped>
.change-font {
  font-family: "Staatliches", sans-serif;
}

.hello {
  background-color: silver;
}
</style>

