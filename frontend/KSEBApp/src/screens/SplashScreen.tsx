import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const SplashScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>시선이음</Text>
      <Text style={styles.subtitle}>보는 것에서, 이해로. 시선을 잇다.</Text>
    </View>
  );
};

export default SplashScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 48,
    fontWeight: 'bold',
    fontFamily: 'AppleSDGothicNeo-Bold', // 혹은 원하는 폰트
    marginBottom: 20,
  },
  subtitle: {
    fontSize: 16,
    color: '#333',
  },
});