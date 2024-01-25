import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ChatBubble = ({ text, sender }) => {
  return (
    <View style={[styles.bubble, sender === 'user' ? styles.userBubble : styles.botBubble]}>
      <Text style={styles.text}>{text}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  bubble: {
    backgroundColor: '#E0E0E0',
    borderRadius: 10,
    margin: 8,
    padding: 12,
    maxWidth: '70%',
  },
  userBubble: {
    alignSelf: 'flex-end',
    backgroundColor: '#4CAF50',
  },
  botBubble: {
    alignSelf: 'flex-start',
  },
  text: {
    color: 'black',
  },
});

export default ChatBubble;
