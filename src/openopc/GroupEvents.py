class GroupEvents:
    def __init__(self):
        self.client = current_client

    def OnDataChange(self, TransactionID, NumItems, ClientHandles, ItemValues, Qualities, TimeStamps):
        self.client.callback_queue.put((TransactionID, ClientHandles, ItemValues, Qualities, TimeStamps))
