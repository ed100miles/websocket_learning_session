// const useStore = create<RFState>((set, get) => ({
//     nodes: initialNodes,
//     edges: initialEdges,
//     websocket: new WebSocket("ws://localhost:6789/"),
//     onNodesChange: (changes: NodeChange[]) => {
//       const ws = get().websocket;
//       ws.send(JSON.stringify(changes));
//       set({
//         nodes: applyNodeChanges(changes, get().nodes),
//       });
//     },...[the rest is the same...]...
