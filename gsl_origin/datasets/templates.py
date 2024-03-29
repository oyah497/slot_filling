from .utils import domain2desc, domainslot2desc, domainslot2example, domainslot2context, domainslot2temp, domainslot2question
from transformers import BartForConditionalGeneration, BartTokenizer

class QueryTemplate:
    def __init__(self, schema):
        if schema == 'slot_desc':
            self.template = 'find the %s in sentence: %s.'
        elif schema == 'slot_desc+domain_desc':
            self.template = 'in domain %s, find the %s in sentence: %s.'
        elif schema == 'example':
            self.template = 'find entities, like %s, in sentence: %s.'
        elif schema == 'context_example':
            self.template = 'find entities, like %s in %s, in sentence: %s.'
        elif schema == 'slot_desc+example':
            self.template = 'find the %s, like %s, in sentence: %s.'
        elif schema == 'slot_desc+context_example':
            self.template = 'find the %s, like %s in %s, in sentence: %s.'
        elif schema == 'slot_desc+domain_desc+context_example':
            self.template = 'in domain %s, find the %s, like %s in %s, in sentence: %s, or not found.'

        elif schema == 'min':
            self.template = '%s.'        
        
        elif schema == 'notSD':
            self.template = 'in domain %s, like %s in %s, in sentence: %s.'


        elif schema == 'proposed_query1':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = 'when he wants to %s, like %s in %s, the %s is ' + f'{tokenizer.mask_token}' + ' in sentence %s.'

        elif schema == 't5_query1':
            self.template = 'in domain %s, find the %s, like %s in %s. the %s is <extra_id_0> in sentence: %s.'
        

        elif schema == 'each_slot':
            model_name = 'facebook/bart-base'
            tokenizer = BartTokenizer.from_pretrained(model_name)
            self.template = '%s sentence: %s. answer: %s sentence: %s. answer: %s'
            self.mask_token = f'{tokenizer.mask_token}'


        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, domain, sentence, slot):
        if domain == 'atis':
            return 'find the %s in sentence: %s.' % (domainslot2desc[domain][slot], sentence)

        if self.schema == 'slot_desc':
            return self.template % (domainslot2desc[domain][slot], sentence)
        elif self.schema == 'slot_desc+domain_desc':
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot], sentence)
        elif self.schema == 'example':
            return self.template % (domainslot2example[domain][slot], sentence)
        elif self.schema == 'context_example':
            return self.template % (domainslot2example[domain][slot], domainslot2context[domain][slot], sentence)
        elif self.schema == 'slot_desc+example':
            return self.template % (domainslot2desc[domain][slot], domainslot2example[domain][slot], sentence)
        elif self.schema == 'slot_desc+context_example':
            return self.template % (domainslot2desc[domain][slot], domainslot2example[domain][slot],
                                    domainslot2context[domain][slot], sentence)
        elif self.schema == 'slot_desc+domain_desc+context_example':
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    sentence)
        
        elif self.schema == 'min':
            return self.template % (sentence)
        
        elif self.schema == 'notSD':
            return self.template % (domain2desc[domain], 
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    sentence)
        elif self.schema == 'proposed_query1':
            return self.template % (domain2desc[domain], #domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    domainslot2desc[domain][slot],
                                    sentence)
        elif self.schema == 't5_query1':
            return self.template % (domain2desc[domain], domainslot2desc[domain][slot],
                                    domainslot2example[domain][slot], domainslot2context[domain][slot],
                                    domainslot2desc[domain][slot],
                                    sentence)



        elif self.schema == 'each_slot':
            return self.template % (domainslot2question[domain][slot],
                                    domainslot2context[domain][slot],
                                    (domainslot2temp[domain][slot] % (domainslot2example[domain][slot])),
                                    sentence,
                                    (domainslot2temp[domain][slot] % (self.mask_token))
                                    )

        else:
            return ValueError('Unknown Error!')


class ResponseTemplate:
    def __init__(self, schema):
        if schema == 'plain':
            self.template = '%s.'
        elif schema == 'proposed':
            self.template = '%s is %s.'
        elif schema == 'proposed2':
            self.template = 'the %s is %s.'
        elif schema == 't5_resp1':
            #self.template = '<extra_id_0> %s <extra_id_1>'
            self.template = '%s.'

        elif schema == 'each_slot':
            pass

        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema

    def __call__(self, domain, sentence, slot, entity):
        if self.schema == 'plain':
            if (entity[0] == ""):
                return 'not found.'
            return self.template % (', '.join(entity))
        elif self.schema == 'proposed':
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))
        elif self.schema == 'proposed2':
            if (entity[0] == ""):
                return 'the ' +  domainslot2desc[domain][slot] + ' is not found.'
            return self.template % (domainslot2desc[domain][slot], ', '.join(entity))

        if self.schema == 't5_resp1':
            return self.template % (', '.join(entity))

        elif self.schema == 'each_slot':
            if entity[0] == "":
                return domainslot2temp[domain][slot] % (domainslot2example[domain][slot])
            return domainslot2temp[domain][slot] % (', '.join(entity))

        else:
            raise ValueError('Unknown Error!')

class DecoderInput:
    def __init__(self, decode_input, schema):
        if schema == 'plain':
            self.template = ''
        elif schema == 'proposed':
            self.template = '%s is'
        elif schema == 'proposed2':
            self.template = 'the %s is'
        else:
            raise ValueError('Unsupported schema: %s.' % schema)
        self.schema = schema
        self.decoder_input = decode_input
    
    def __call__(self, domain, sentence, slot, entity):

        if self.decoder_input == False:
            return ''
        elif self.schema == 'plain':
            return self.template
        elif self.schema == 'proposed':
            return self.template % (domainslot2desc[domain][slot])
        elif self.schema == 'proposed2':
            return self.template % (domainslot2desc[domain][slot])
        else:
            raise ValueError('Unknown Error!')
