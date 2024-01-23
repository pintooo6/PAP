import React, { useState } from 'react';
import { View, StyleSheet, TextInput, Button } from 'react-native';

const ChatInput = () => {
  const [message, setMessage] = useState('');

  const handleSendMessage = () => {
    // Send message to the chatbot
    setMessage('');
  };

  return (
    <View style={styles.inputContainer}>
      <TextInput
        placeholder="Enter your message"
        value={message}
        onChangeText={(newMessage) => setMessage(newMessage)}
        onSubmitEditing={handleSendMessage}
      />
      <Button title="Send" onPress={handleSendMessage} />
    </View>
  );
};

const styles = StyleSheet.create({
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
});

export default ChatInput;
