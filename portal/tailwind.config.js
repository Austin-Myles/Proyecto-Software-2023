module.exports = {
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}", ],
    daisyui: {
        themes:[
            {
                mytheme: {
                    "primary": "#f3f4f6",
                    "secondary": "#60a5fa",
                    "accent": "#facc15",
                    "neutral": "#2563eb",
                    "base-100": "#f3f4f6",
                    "info": "#0369a1",
                    "success": "#009677",
                    "warning": "#ffb100",
                    "error": "#ff525d",
                             },
            },
        ]
    },
    plugins: [require("daisyui")],
    theme: {
        extend: {
            width:{
                'half': '50vw',
            },
        },
    }
}
