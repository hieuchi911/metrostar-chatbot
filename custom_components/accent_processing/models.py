import tensorflow as tf
from modules import Decoder, create_padding_mask


class Transformer(tf.keras.Model):
    def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size,
                 target_vocab_size, pe_input, rate=0.1):
        super(Transformer, self).__init__()

        # self.encoder = Encoder(num_layers, d_model, num_heads, dff,
        #                        input_vocab_size, pe_input, rate)

        self.decoder = Decoder(num_layers, d_model, num_heads, dff,
                               input_vocab_size, pe_input, rate)

        self.final_layer = tf.keras.layers.Dense(target_vocab_size)

    def call(self, inp, training):
        # Keras models prefer if you pass all your inputs in the first argument

        dec_inp_padding_mask = self.create_masks(inp)

        # print('enc_padding_mask: ', enc_padding_mask)
        # enc_output = self.encoder(inp, training, enc_padding_mask)  # (batch_size, inp_seq_len, d_model)

        # dec_output.shape == (batch_size, tar_seq_len, d_model)
        dec_output = self.decoder(inp, training, dec_inp_padding_mask)

        final_output = self.final_layer(dec_output)  # (batch_size, tar_seq_len, target_vocab_size)

        return final_output

    def create_masks(self, inp):
        # Encoder padding mask
        # enc_padding_mask = create_padding_mask(inp)

        # Used in the 2nd attention block in the decoder.
        # This padding mask is used to mask the encoder outputs.
        dec_inp_padding_mask = create_padding_mask(inp)

        return dec_inp_padding_mask