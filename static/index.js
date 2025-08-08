function port(Data, Route){
    async function Send_Receive(Data, Route) {
        try {
            const res = await fetch(Route, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ data: Data })
            });

            const result = await res.json();
            return result;
        } catch (err) {
            console.error("Error:", err);
            return null;
        }
    }

    Send_Receive("Hello", "/send").then(result => {
        console.log(result);
    });
};

port("Hello","/send")