import { firebase } from "@firebase/app";
import "@firebase/firestore";

const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyAEGcm_zjg29OZweIEJIMnRQ4wlOM8JI1k",
  authDomain: "zengen.firebaseapp.com",
  databaseURL: "https://zengen.firebaseio.com",
  projectId: "zengen",
  storageBucket: "zengen.appspot.com",
  messagingSenderId: "533965407080",
  appId: "1:533965407080:web:652470f52c375066"
});

const db = firebaseApp.firestore();
const auth = firebaseApp.auth();
const currentUser = auth.currentUser();

export {
  db,
  auth,
  currentUser
}