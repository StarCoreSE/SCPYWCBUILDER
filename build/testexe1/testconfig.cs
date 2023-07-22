private AmmoDef Example_Ammo => new AmmoDef
{
    AmmoMagazine = "Energy",
    BaseDamage = 8023,
    HardPointUsable = true,
    NoGridOrArmorScaling = true, 
    Trajectory = new TrajectoryDef
    {
		MaxLifeTime = 3600,
		MaxTrajectory = 4884,
		DesiredSpeed = 6628,
    },
    AmmoGraphics = new GraphicDef
    {
	VisualProbability = 1f,
	Lines = new LineDef
	{
	   Tracer = new TracerBaseDef
	   {
	       Enable = true,
	       Length = 10f,
	       Width = 0.1f,
	       Color = Color(red: 20, green: 55, blue: 199, alpha: 1), green: 55, blue: 199, alpha: 1),
	       Textures = new[] {"ProjectileTrailLine",},
	   },
	},
    },
};