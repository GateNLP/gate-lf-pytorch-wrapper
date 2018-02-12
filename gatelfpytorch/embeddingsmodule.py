import torch


class EmbeddingsModule(torch.nn.Module):

    def __init__(self, vocab):
        """If vocab.train is yes new embeddings will get learned, starting off with random vectors if no pretrained
        embeddings are given, otherwise the pretrained embeddings will be used where possible.
        If train is no, then no training will be done and the pretrained embeddings will be used only.
        If train is mapping then a mapping is learned from pretrained embeddings to our own embeddings.
        NOTE: this should all happen automatically by inspecting and using the vocab instance.
        TODO: currently only newly trained embeddings supported because we do not have support from Vocab yet!!
        """
        super().__init__()
        self.emb_id = vocab.emb_id
        self.emb_train = vocab.emb_train
        self.emb_dim = vocab.emb_dim
        if not self.emb_dim:
            self.emb_dim = 100
        self.emb_size = vocab.n
        self.module = torch.nn.Embedding(self.emb_size, embedding_dim=self.emb_dim, padding_idx=0)

    def forward(self, batch):
        return self.module(batch)
