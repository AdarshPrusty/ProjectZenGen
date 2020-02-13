<template>
    <div>
        <Main></Main>
        <v-card height = '10vh' color = 'rgba(0,0,0,0)' flat=true></v-card>
        <v-row justify='center'>
            <v-spacer></v-spacer>
            <v-card min-height="80vh" width="70vw" color="rgba(0,0,0,0.4)" outlined tile=true>
                <v-card  width='20vw'>
                        <form @submit="addUsername(username, password)">
                            <input class="input" v-model="username" type="text" placeholder="Email"><br>
                            <input class="input" v-model="password" type="password" placeholder="Password"><br>
                            <v-btn type="submit" class="button">Press</v-btn>
                        </form>
                </v-card>

                <p>Create an account if you don't already have one</p>
            </v-card>
            <v-spacer></v-spacer>
        </v-row>
    </div>
</template>

<script>
import Main from '../components/Main'
import { db } from '../router'

export default {
    name: 'Login',
    components: {
        Main
    },
    methods: {
        addUsername (username, password) {
            db.collection('users').add({ username, password })
        } 
    }
}
</script>