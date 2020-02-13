<template>
    <div>
        <Main></Main>
        <v-card height = '10vh' color = 'rgba(0,0,0,0)' flat=true></v-card>
        <v-row justify='center'>
            <v-spacer></v-spacer>
            <v-card min-height="80vh" width="70vw" color="rgba(0,0,0,0.4)" outlined tile=true>
            </v-card>
            <v-spacer></v-spacer>
        </v-row>
    </div>
</template>

<script>
import Main from '../components/Main'

export default {
    name: 'Register',
    components: {
        Main
    }
}
</script>