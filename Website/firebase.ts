// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCZCwALOMrUsyHhuzAr9OcF2A-YKKlaHO4",
  authDomain: "ai-caseathon.firebaseapp.com",
  projectId: "ai-caseathon",
  storageBucket: "ai-caseathon.firebasestorage.app",
  messagingSenderId: "937779777255",
  appId: "1:937779777255:web:4950006ea3b843d072dc42",
  measurementId: "G-3ND6T6Z9X3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app)
const analytics = getAnalytics(app);