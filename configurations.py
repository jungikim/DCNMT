def get_config():
    config = {}
    # Where to save model, this corresponds to 'prefix' in groundhog
    config['saveto'] = 'dcnmt_en2fr'

    # prepare data
    config['source_language'] = 'en'
    config['target_language'] = 'fr'

    # Model related -----------------------------------------------------------

    # Sequences longer than this will be discarded
    config['max_src_seq_char_len'] = 300
    config['max_src_seq_word_len'] = 50
    config['max_trg_seq_char_len'] = 300
    config['max_trg_seq_word_len'] = 50

    # Number of hidden units in encoder/decoder GRU
    config['src_dgru_nhids'] = 512
    config['enc_nhids'] = 1024
    config['dec_nhids'] = 1024
    config['trg_dgru_nhids'] = 512
    config['trg_igru_nhids'] = 1024


    # Dimension of the word embedding matrix in encoder/decoder
    config['enc_embed'] = 64
    config['dec_embed'] = 64
    config['src_dgru_depth'] = 2
    config['bidir_encoder_depth'] = 2
    config['transition_depth'] = 1
    config['trg_dgru_depth'] = 1
    config['trg_igru_depth'] = 1


    # Optimization related ----------------------------------------------------

    # Batch size
    config['batch_size'] = 80

    # This many batches will be read ahead and sorted
    config['sort_k_batches'] = 12

    # Optimization step rule
    config['step_rule'] = 'AdaDelta'

    # Gradient clipping threshold
    config['step_clipping'] = 1.

    # Std of weight initialization
    config['weight_scale'] = 0.01

    # Regularization related --------------------------------------------------

    # Weight noise flag for feed forward layers
    config['weight_noise_ff'] = False

    # Weight noise flag for recurrent layers
    config['weight_noise_rec'] = False


    # Vocabulary/dataset related ----------------------------------------------

    # Root directory for dataset
    datadir = './data/'

    # Module name of the stream that will be used
    config['stream'] = 'stream'

    # Source and target vocabularies
    config['src_vocab'] = datadir + 'vocab.{}-{}.{}.pkl'.format(config['source_language'], config['target_language'],
                                                                config['source_language'])
    config['trg_vocab'] = datadir + 'vocab.{}-{}.{}.pkl'.format(config['source_language'], config['target_language'],
                                                                config['target_language'])

    # Source and target datasets
    config['src_data'] = datadir + 'all.en-fr.en.tok.shuf'
    config['trg_data'] = datadir + 'all.en-fr.fr.tok.shuf'

    # Source and target vocabulary sizes, should include bos, eos, unk tokens
    config['src_vocab_size'] = 120
    config['trg_vocab_size'] = 120

    # Special tokens and indexes
    config['unk_id'] = 1
    config['bos_token'] = '<S>'
    config['eos_token'] = '</S>'
    config['unk_token'] = '<UNK>'

    # Early stopping based on val related ------------------------------------

    # Normalize cost according to sequence length after beam-search
    config['normalized_val'] = True

    # Normalize cost according to sequence length after beam-search
    config['normalized_bleu'] = True

    # Bleu script that will be used (moses multi-perl in this case)
    config['bleu_script'] = datadir + 'multi-bleu.perl'

    # Validation set source file
    config['val_set'] = datadir + 'newstest2013.en.tok'

    # Validation set gold file
    config['val_set_grndtruth'] = datadir + 'newstest2013.fr.tok'

    # Test set source file
    config['test_set'] = datadir + 'newstest2014.en.tok'

    # Test set gold file
    config['test_set_grndtruth'] = datadir + 'newstest2014.fr.tok'

    config['validate'] = True

    # Print validation output to file
    config['output_val_set'] = True

    # Validation output file
    config['val_set_out'] = config['saveto'] + '/validation_out.txt'

    # Validation output file
    config['test_set_out'] = config['saveto'] + '/test_out.txt'

    # Beam-size
    config['beam_size'] = 12

    # Timing/monitoring related -----------------------------------------------

    # Maximum number of updates
    config['finish_after'] = 432000

    # Reload model from files if exist
    config['reload'] = True

    # Save model after this many updates
    config['save_freq'] = 500

    # Show samples from model after this many updates
    config['sampling_freq'] = 30

    # Show this many samples at each sampling
    config['hook_samples'] = 2

    config['bleu_val_freq'] = 18000
    # Start validation after this many updates
    config['val_burn_in'] = 70000

    return config
