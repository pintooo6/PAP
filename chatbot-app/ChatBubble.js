import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ChatBubble = ({ message, isUserMessage }) => {
  const bubbleStyle = isUserMessage ? { backgroundColor: '#ddd' } : { backgroundColor: '#eee' };
  const textStyle = { fontSize: 16, padding: 10 };

  return (
    <View style={bubbleStyle}>
      <Text style={textStyle}>{message}</Text>
    </View>
  );
};

export default ChatBubble;
