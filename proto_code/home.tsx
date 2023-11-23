// export default function Home() {
//     let {
//       nodes,
//       edges,
//       onConnect,
//       onNodesChange,
//       onEdgesChange,
//       onAddNodes: handleAddNodes,
//       nodeTypes,
//       websocket,
//     } = useStore((state) => state, shallow);
//     const router = useRouter();
//     // const websocket = new WebSocket("ws://localhost:6789/");
//     websocket.onmessage = ({data})=>{
//       // const recievedChanges = JSON.parse(data).nodeChange
//       console.log(data)
//       onNodesChange(JSON.parse(data));
//     }
