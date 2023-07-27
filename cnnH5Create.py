from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define the CNN architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model on the thermal camera data
model.fit(X_train, y_train, epochs=10, batch_size=32)

# evaluate the model on test set
score = model.evaluate(X_test, y_test, batch_size=32)

# use the trained model to classify new images
predictions = model.predict(new_images)



# used keras for creating h5 file for clasification perpose