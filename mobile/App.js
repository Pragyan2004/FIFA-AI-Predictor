import React from 'react';
import { SafeAreaView, Text, View, StyleSheet, TouchableOpacity } from 'react-native';

// Phase 7: React Native Mobile Application Scaffold
// This is the entry point for the iOS and Android application.

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>FIFA AI Predictor</Text>
        <Text style={styles.subtitle}>Mobile Edition</Text>
      </View>
      
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Live Match</Text>
        <Text style={styles.matchText}>Argentina 2 - 1 France (78')</Text>
        <TouchableOpacity style={styles.button}>
          <Text style={styles.buttonText}>View AI Analysis</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0f172a' },
  header: { padding: 20, alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#38bdf8' },
  subtitle: { fontSize: 16, color: '#94a3b8' },
  card: { margin: 20, padding: 20, backgroundColor: '#1e293b', borderRadius: 15, borderColor: '#334155', borderWidth: 1 },
  cardTitle: { color: '#cbd5e1', fontSize: 14, marginBottom: 10, fontWeight: 'bold', textTransform: 'uppercase' },
  matchText: { color: 'white', fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  button: { backgroundColor: '#0ea5e9', padding: 15, borderRadius: 10, alignItems: 'center' },
  buttonText: { color: 'white', fontWeight: 'bold' }
});
