from keras.models import load_model, Model
from keras.layers import Dense

# Load the pre-trained model
pretrained_model = load_model('path_to_pretrained_model.h5')

# Freeze the layers
for layer in pretrained_model.layers:
    layer.trainable = False

# Add a new output layer
num_classes = 2 # example for cat and dog classification
new_output = Dense(num_classes, activation='softmax')(pretrained_model.layers[-2].output)

# Create the new model
model = Model(inputs=pretrained_model.input, outputs=new_output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(new_data, new_labels, epochs=10, batch_size=32, validation_data=(val_data, val_labels))



# since there are more than one h5 file  give the  path_to_pretrained_model.h5