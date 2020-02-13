<template>
  <div class="home">
    <Main></Main>
    <v-card height = '20vh' color = 'rgba(0,0,0,0)' flat=true></v-card>
    <TextBox v-bind:quote = "quote"></TextBox>
    <v-card height = '10vh' color = 'rgba(0,0,0,0)' flat=true></v-card>
    <Awaken></Awaken>
  </div>
</template>

<script>
import Main from "@/components/Main";
import TextBox from "@/components/TextBox";
import Awaken from "@/components/Awakening";

export default {
  name: 'Home',
  components: {
    Main,
    TextBox,
    Awaken
  },
  data (){
    return {
      quote: 'A storm brewed overhead, cutting the fortress and its grand towers an imperious shadow '
    }
  }
}
</script>
