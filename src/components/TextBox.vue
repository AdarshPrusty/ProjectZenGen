<template>
    <div id='textbox'>
            <v-row justify='center'>
                <v-spacer></v-spacer>
                <v-card min-height="15vh" max-height="25vh" width="70vw" color="rgba(0,0,0,0.4)" outlined tile=true>
                    <h1>{{ quote }}</h1>
                </v-card>
                <v-spacer></v-spacer>
            </v-row>

    </div>
</template>

<script>
export default {
    name:"TextBox",
    props: {
        quote: {
            type: String
        }
    }
}
</script>

<style scoped>
h1 {
   color: white;
   font-size: 5vh;
}

#textbox {
    text-align: center;
}
</style>